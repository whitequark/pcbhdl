# Copyright (C) 2011-2013 Sebastien Bourdeauducq.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import inspect
from opcode import opname
from collections import defaultdict


def get_var_name(frame):
    code = frame.f_code
    call_index = frame.f_lasti
    call_opc = opname[code.co_code[call_index]]
    if call_opc != "CALL_FUNCTION" and call_opc != "CALL_FUNCTION_VAR":
        return None
    index = call_index+3
    while True:
        opc = opname[code.co_code[index]]
        if opc == "STORE_NAME" or opc == "STORE_ATTR":
            name_index = int(code.co_code[index+1])
            return code.co_names[name_index]
        elif opc == "STORE_FAST":
            name_index = int(code.co_code[index+1])
            return code.co_varnames[name_index]
        elif opc == "STORE_DEREF":
            name_index = int(code.co_code[index+1])
            return code.co_cellvars[name_index]
        elif opc == "LOAD_GLOBAL" or opc == "LOAD_ATTR" or opc == "LOAD_FAST" or opc == "LOAD_DEREF":
            index += 3
        elif opc == "DUP_TOP":
            index += 1
        elif opc == "BUILD_LIST":
            index += 3
        else:
            return None


def get_obj_var_name(override=None, default=None):
    if override:
        return override

    frame = inspect.currentframe().f_back
    # We can be called via derived classes. Go back the stack frames
    # until we reach the first class that does not inherit from us.
    ourclass = frame.f_locals["self"].__class__
    while "self" in frame.f_locals and isinstance(frame.f_locals["self"], ourclass):
        frame = frame.f_back

    vn = get_var_name(frame)
    if vn is None:
        vn = default
    return vn


def index_id(l, obj):
    for n, e in enumerate(l):
        if id(e) == id(obj):
            return n
    raise ValueError


name_to_idx = defaultdict(int)
classname_to_objs = dict()

def trace_back(varname=None):
    result = []
    frame = inspect.currentframe().f_back.f_back
    while frame is not None:
        if varname is None:
            varname = get_var_name(frame)
        if varname is not None:
            result.insert(0, (varname, name_to_idx[varname]))
            name_to_idx[varname] += 1

        try:
            obj = frame.f_locals["self"]
        except KeyError:
            obj = None
        if hasattr(obj, "__del__"):
            obj = None

        if obj is None:
            if varname is not None:
                coname = frame.f_code.co_name
                if coname == "<module>":
                    modules = frame.f_globals["__name__"]
                    modules = modules.split(".")
                    coname = modules[len(modules)-1]
                result.insert(0, (coname, name_to_idx[coname]))
                name_to_idx[coname] += 1
        else:
            classname = obj.__class__.__name__
            try:
                objs = classname_to_objs[classname]
            except KeyError:
                classname_to_objs[classname] = [obj]
                idx = 0
            else:
                try:
                    idx = index_id(objs, obj)
                except ValueError:
                    idx = len(objs)
                    objs.append(obj)
            result.insert(0, (classname, idx))

        varname = None
        frame = frame.f_back
    return result
