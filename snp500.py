from datapackage import Package


def get_symbols():
    package = Package('https://datahub.io/core/s-and-p-500-companies/datapackage.json')
    for resource in package.resources:
        if resource.descriptor['datahub']['type'] == 'derived/csv':
            res = list(map(lambda stock: stock[0], resource.read()))
            print("symbols count = {}".format(len(res)))
            return res
