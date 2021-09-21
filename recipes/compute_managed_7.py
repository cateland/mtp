
import dataiku
from dataiku import recipe
in0 = recipe.get_inputs()[0]
df = in0.get_dataframe()
out0 = recipe.get_outputs()[0]
out0.write_with_schema(df)
out1 = recipe.get_outputs()[1]
out1.write_with_schema(df)
