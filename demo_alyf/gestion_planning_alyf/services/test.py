
import Module

variables = {}
for i in range(5):
    var_name = i
    variables[var_name] = Module.Module("poc", i, i+1, "session", [], [])



print(variables[1].get_nom_module())