'''

vandal - Data science, Data manipulation and Machine learning library.
=====================================================================

This is a connection to the __init__ file of the vandal library.

AVAILABLE FEATURES IN THE LIBRARY:

	TOOLKIT (MODULE FUNCTIONS)
	--------------------------

	set of available data manipulation functions from the vandal library.
		print(help(any_function_listed_below)) in order to see the function details or print(help(vandal.toolkit)) for all functions at once.

		FUNCTIONS (ACCESSIBLE DIRECTLY FROM THE LIBRARY)
		------------------------------------------------

		random_value(mean, st_dev, **rounded) - gives a random value of mean and standard deviation inputed, if rounded = 'y', value will be rounded.

		random_pool(mean, st_dev, pool_size, **rounded) - gives random values of mean and standard deviation inputed for the amount of values defined in the pool size, if rounded = 'y', values will be rounded.

		split_values(data, split_method) - splits the data using a split method character.

		join_values(data, join_method) - joins the data using a join metod character.

		replace_values(data, replaced_value, replacing_value) - replaces a defined value with a desired value.

		list_sort(data, array) - manually sorts data depending on defined array of indexes.

		index_sort(data, split_method, index_array) - sorts the indicies in a list of values based on the index array defined as [x,x,x].

		auto_sort(data, split_method, trigger = lambda x: x[0]) - automatically splits all values in a list and sorts them based on the added trigger as lambda x: [x[i], x[i]] and joins them back together.

	MONTECARLO (OBJECT)
	-------------------

	vandal.MonteCarlo is a module for performing the Monte Carlo simulation over the defined data with a lot of useful features.
		print(help(vandal.MonteCarlo)) in order to see available features.

	EOQ (OBJECT)
	------------

	vandal.EOQ is a module for finding an Economic order quantity over the defined data with a lot of useful features.
		print(help(vandal.EOQ)) in order to see available features.

	Dijkstra (OBJECT)
	-----------------

	vandal.Dijkstra is a module for finding the optimal route between the defined nodes from the place of origin to the final destination.
		print(help(vandal.Dijkstra)) in order to see available features.

	CLI (EXECUTABLE FUNCTION)
	-------------------------

	vandal.CLI is an executable function that runs the Command Line Inerface of the vandal package.
		print(help(vandal.CLI)) in order to see available features.

'''

# ignore __pycache__ from forming inside the library directory.
import sys
sys.dont_write_bytecode = True

# meta data imports from the vandal library.
from .misc._meta import (
    __author__,
    __copyright__,
    __credits__,
    __license__,
    __version__,
    __documentation__,
    __contact__,
    __donate__,
)

# vandalCLI.exe version.
from .cli.cli import __CLIversion__

# object and module imports.
from .hub import toolkit
from .objects.eoq import EOQ
from .objects.montecarlo import MonteCarlo
from .objects.dijkstra import Dijkstra

# hub imports.
from .hub.toolkit import (
    random_value,
    random_pool,
    split_values,
    join_values,
    replace_values,
    list_sort,
    index_sort,
    auto_sort,
)

# cli imports
from .cli.cli import *

# all relevant contents.
__all__ = [
    random_value,
    random_pool,
    split_values,
    join_values,
    replace_values,
    list_sort,
    index_sort,
    auto_sort,
    toolkit,
    MonteCarlo,
    EOQ,
    Dijkstra,
    CLI,
]