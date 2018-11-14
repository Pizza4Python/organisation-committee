import sys
import random

def roll_dice(sides, throws):
	"""Short summary.

	Parameters
	----------
	sides : int
	Number of sides of the dice.
	throws : int
	How many times the dice is rolled.

	Returns
	-------
	list
	List with the dice score of each throw.
	"""

	# If you want, uncomment the following line to set a random seed
	# random.seed(42)

	results = []
	for throw in range(throws):
		results.append(random.randint(1,sides))

	return results


def fetch_parameters():
	"""Short summary.

	Returns
	-------
	int, int
	The fetched (positional) parameters from the terminal, converted to
	integers.
	"""
	sides = int(sys.argv[1])
	throws = int(sys.argv[2])

	return sides, throws


def divide_in_two_subsets(throws, throw_results):
    """Short summary.

    Parameters
    ----------
    throws : int
        How many times the dice is rolled.
    throw_results : list
        List with the dice score of each throw.

    Returns
    -------
    list, list
        The two subsets of the dice rolls.

    """
	# Generate a list and fill it with 0s and 1s, as many as rools have occurr
	mask = []
	for throw in range(throws):
		mask.append(random.randint(0,1))

	# Generate the lists where your subsets will live and move the values of
	# throw_results to one or the other depending on the value found in mask in
	# that same position.
	subset0 = []
	subset1 = []
	for i, score in enumerate(throw_results):
		if mask[i] == 0:
			subset0.append(score)
		elif mask[i] == 1:
			subset1.append(score)
		else:
			sys.exit("This should not happen, check your code")

	return subset0, subset1


def main():
	faces, times = fetch_parameters()
	scores = roll_dice(faces, times)
	print(scores)

	mask0, mask1 = divide_in_two_subsets(times, scores)
	print(mask0)
	print(mask1)


# This condition makes python only run the script when it is called on the
# top level. This is important to understand if you ever write a package to be
# used separately
if __name__ == '__main__':
	main()
