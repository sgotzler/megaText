# Mapping the Television Mega-Text

DOI #**add DOI when KiltHub is deposit is live**

Welcome to the Git Hub repository for the "Mapping the Television Mega-Text" project. This repository contains a release of our dataset of programming information about 1950's television. This dataset was created by merging together metadata gathered from IMDB.com and elsewhere in an effort to collect, collate, and publish a compendium of metadata about television in the fifties, much of which does not survive in any watchable form today.

In this repository, you will find files containing all of the records from our dataset as CSVs, as well as a description of the data, the data structure, and some guidelines on using the data. Please take a minute to briefly read over the sections below carefully.

Additionally, the repository also contains the Jupyter Notebooks that we wrote in Python3 in order to merge the different sources of television metadata into a single dataset, and that we also used to run a preliminary round of textual analysis working-class content in the Action & Adventure genres.

The notebooks for these python scripts and their accompanying documentation are located in the "merge" and "analysis" folders respectively. The notebook merge.ipynb pulss from a local sqlite database of imdb metadata downloaded on 09/2017.

## Data Structure

The data is released as a CSV dump, "title5.csv" contains the merged dataset of 1950's programming, and can be found in the merge folder.

Programming information was gathered from 2 sources:
- (1) a bulk download of publicly available data from IMDB
- (2) a public domain scan of Vincent Terrace's [*Encyclopedia Of Television Shows 1925-2007*](https://archive.org/details/EncyclopediaOfTelevisionShows1925Through2007V.142009P.1855) on the Internet Archive.

### Metadata Format

The merged dataset contains program information for 2563 records. Each program record contains 14 different metadata attributes.

In the dataset, these series are displayed as the following columns:

| **Series** | **Description** |
-------------|-------------|
| realtitle   | assigned by us; defaults to Encyclopedia's title when matched otherwise displays imdb title. |
| program_type | from Encyclopedia |
| program_genre | from Encyclopedia |
| network | from Encyclopedia |
| program_description | from Encyclopedia |
| first_air_year | from Encyclopedia |
| last_air_year | from Encyclopedia |
| genre(3) | from IMDB |
| plot(98) | from IMDB |
| trivia | from IMDB |
| program_title | from Encyclopedia |
| movie_id | from IMDB |
| kind_id | from IMDB; denotes the type of programming content, i.e. series, episode or tv movie. |
| title | from IMDB |

#### Note: Program Genre

There is often more than one genre tags  associated with a program. This include the single genre assignment taken from Terrace, and the multiple genre tags assigned on IMDB. In the CSV, these are separated into separate series, and appear as two different columns. The genre tags from Terrace appear under "program_genre," while the IMDB genre tags are collated under genre(3).

#### Note: Program Description

Note that the program description field contains the richest amount of textual information pertaining to a given program. Note also, that a range of different sub-types of metadata exist within "program_description" as well. In addition to the prose descriptions of a given program's premise, flavor, and content, the description field may also contain numerous lists of categorized participants and creators. These lists are denoted by unique titles followed by a colon, and may be separated out manually by this punctuation. Types of participant categories occurring in the "program_description" field include:

- "Host:"
- "Hostess:"
- "Starring:"
- "Regulars:"
- "Guests:"
- "Music:"
- "Orchestra:"
- "Vocalists:"

## Dataset Integrity

This dataset is provided for the purposes of further exploration, education, experimentation regarding the largely lost world of early television programming.

If you have identified errors in the dataset, or have additional information to add, we welcome your feedback! Please contact us at mailto:kn4@andrew.cmu.edu

Thanks!

## Pull Requests

Please note that we will not accept pull requests for the data in this repository.

If you have corrections, please email them to us at mailto:kn4@andrew.cmu.edu and we will forward them to the appropriate department for correction and inclusion in a future release.

## Attribution

Our dataset is being offered under the CC-BY 4.0 Creative Commons License. [![License: CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/

We respectfully ask that you acknowledge "Mapping the Television Mega-Text" and dSHARP at CMU as a source wherever possible, in order to preserve a link to the dataset.

If this data is to be cited in a publication, please cite it using this **DOI: ADD DOI from KiltHub**.

Use of this dataset does not grant or imply the approval, commission, or support of your work by the researchers, Carnegie Mellon University, or dSHARP at CMU. If you transform or modify to the dataset, you must clearly distinguish the resulting work as having been modified from the dSHARP hosted dataset.

## Acknowledgement

The writers would like to thank and acknowledge the funding of this project by the Andrew W. Mellon Foundation, as well as the technical and professional support of digital humanists and specialists at Carnegie Mellon University and the University of Pittsburgh including Scott Weingart, Daniel J. Evans, Emma Slayton, Matt Lavin, and Matthew Lincoln.
