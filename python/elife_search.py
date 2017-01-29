__author__ = 'ps14'

# search the eLife corpus for articles matching a particular rsid

# curl -v "http://prod--gateway.elifesciences.org/search?for=dna" | python -m json.tool

import subprocess

import json


def eLifeSearch(rsid):
    cmd = "curl -v 'http://prod--gateway.elifesciences.org/search?for={}' | python -m json.tool".format(rsid)
    print(cmd)
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    # output is a json
    results_dict = json.loads(output)

    results = []

    for item in results_dict['items']:
        res_dict = {'rsid': rsid, 'type': item['type'], 'title': item["title"],
                   'pdf': item["pdf"],
                   'date_published': item["published"]}
        results.append(res_dict)

    print(results)

    return results


if __name__ == "__main__":
    eLifeSearch("rs1743292")
    eLifeSearch("rs72921001")