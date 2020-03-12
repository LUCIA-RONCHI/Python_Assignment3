class salad():

    import os
    import glob
    import re

    # Initialize class
    def __init__(self):
        self.path = ""
        self.salad_ingredients = []
        self.n_items = []

    # Define function to write files
    def write(self, path, salad_ingredients, n_items):

        # Set path to read and write files
        self.path = path

        # Check whether both lists are of the same length, otherwise return an error
        assert len(salad_ingredients) == len(n_items), "Not Cool"

        # Make a nwe folder only if doesn't already exist in that path
        os.makedirs(self.path, exist_ok = True)

        # Write files
        # Go ingredient by ingredient
        for k in range(len(salad_ingredients)):
            # Go amount by amount
            for j in range(n_items[k]):
                # create file with specific format
                file_name = salad_ingredients[k] + '{:0>2}'.format(j) + '.salad'
                # Write file
                f = open(os.path.join(self.path,file_name), "w+")
                f.close

    # Define function to read files
    def read(self, path):

        # Create a list with all file names ending with .salad
        flist = glob.glob(os.path.join(path, '*.salad'))

        # Initialize empty result lists
        ingredient = []
        ingredient_number = []

        # Go file by file, parsing ingredient and file number
        for file in flist:

            # Create regex of useful parts of the string
            regex = r"(\w*)(\d\d)"

            # Search file name
            x = re.search(regex, file)

            # Parse file name and add to corresponding result list
            ingredient.append(x.group(1))
            ingredient_number.append(x.group(2))

            # Create dictionary
            res_zip = zip(ingredient, ingredient_number)
            res_dict = dict()
            for k,v in res_zip:
                res_dict.setdefault(k, []).append(v)

        return res_dict
