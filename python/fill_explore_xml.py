__author__ = 'ps14'

import re

# pass xml 'skeleton' where genotype to fill in should have the tag: {rs99999}
# uses genotype and str.format to personalize the xml skeleton

def personalize_xml(xml_skeleton, genotype):

    all_rsids = list(set(re.findall("rs[0-9]*", open(xml_skeleton).read())))

    g = {k: k+genotype[k] for k in genotype if k in all_rsids}

    # fill in the xml tags
    xml_personalized = open(xml_skeleton).read().format(**g)

    return(xml_personalized)

if __name__ == "__main__":

    # xml skeleton to fill in
    xml_skeleton = "/Users/ps14/explore/lens-explore/data/taste_prefs_skeleton.xml"

    # load user genotype
    dm = open('/Users/ps14/explore/lens-explore/data/dm_23andme_v3_110219.txt','r')

    genotype = {}
    for line in dm:
        if line.startswith('#'):
            continue
        line = line.split("\t")
        genotype[line[0]] = line[3].rstrip()

    personalize_xml(xml_skeleton, genotype)