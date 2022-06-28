import pandas


def readfile(file_path):
    list_info = []
    try:
        file1 = pandas.read_csv(file_path,encoding='GBK')
        for i in file1.index.values:
            dict1 = file1.loc[i].to_dict()
            list_info.append(dict1)
        # print(list_info)
        return list_info

    except:
        try:
            file2 = pandas.read_excel(file_path)
            for i in file2.index.values:
                dict1 = file2.loc[i].to_dict()
                list_info.append(dict1)
            # print(list_info)
            return list_info

        except:
            print("文件格式错误")
    # finally:
    #     return list_info


if __name__ == '__main__':
    print(readfile(r'../data/login_admin_info.xlsx'))
    # readfile(r'../data/user_info.xlsx')
