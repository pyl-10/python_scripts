from configparser import ConfigParser

def read_db_config(filename="config.ini", section="mysql"):
    #  解析并读取 ini 配置文件
    parser = ConfigParser()
    parser.read(filename)

    # get section
    if parser.has_section(section):
        items = parser.items(section)
    else:
        raise Exception("{0} not found in the {1} file".format(section, filename))
    return dict(items)

if __name__ == "__main__":
    print(read_db_config())