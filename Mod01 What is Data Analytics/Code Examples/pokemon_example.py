# import the thing that lets us use data frames

# use Python's package manager (pip) to install a package that we need
# pip install <<PACKAGE NAME>>

# pandas
# pip install pandas
# "as pd" makes "pd" a nickname for the package
import pandas as pd

df = pd.read_csv('./AllPokemon.csv')

print(df)