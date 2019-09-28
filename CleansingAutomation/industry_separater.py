from table import Table, tsvtotable
import constant as cs
import numpy as np


def separate_industry(table):
    # Create new table with headers from the old one
    new_table = Table(np.array([table.header()]))

    # Find index of target column
    industry_index = np.where(table.header() == "Industry")[0][0]

    new_body = list()
    for row in table.body():
        # split and strip industries separated by comma
        industries_str = row[industry_index]
        industries = [x.strip() for x in str(industries_str).split(",")]

        # create duplicate rows for each industries and append to new_body
        for industry in industries:
            temp_row = np.copy(row)
            temp_row[industry_index] = industry
            new_body.append(temp_row)

    # concatenate new_body to the data in new table
    new_table.concatenate(new_body)
    return new_table


def main():
    degree_table = tsvtotable("./../" + cs.degree_file_name)
    new_degree_table = separate_industry(degree_table)

    # non_degree_table = tsvtotable("./../" + cs.non_degree_file_name)
    # new_non_degree_table = separate_industry(non_degree_table)

    np.savetxt("degree_split.tsv", new_degree_table.data, delimiter="\t", fmt="%s", encoding='utf-8')
    np.savetxt("degree_split.csv", new_degree_table.data, delimiter=",", fmt="%s", encoding='utf-8')
    # np.savetxt("non_degree_split.tsv", new_non_degree_table.data, delimiter="\t", fmt="%s", encoding='utf-8')

main()
