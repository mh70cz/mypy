# -*- coding: utf-8 -*-
"""
Bite 166. Complete a tox ini file parser class
"""
import configparser


class ToxIniParser:

    def __init__(self, ini_file):
        """Use configparser to load ini_file into self.config"""
        self.config = configparser.ConfigParser()
        self.config.read(ini_file)
        

    @property
    def number_of_sections(self):
        """Return the number of sections in the ini file.
           New to properties? -> https://pybit.es/property-decorator.html
        """
        sections = self.config.sections()
        return len(sections)

    @property
    def environments(self):
        """Return a list of environments
           (= "envlist" attribute of [tox] section)"""
        env_txt = self.config["tox"]["envlist"]
        env_lst_raw = env_txt.strip().replace("\n",",").split(",")
        env_lst = [x.strip() for x in env_lst_raw if x != ""]
        return env_lst

    @property
    def base_python_versions(self):
        """Return a list of all basepython across the ini file"""
        sections = self.config.sections()
        bp_set = set()
        for section in sections:
            if "basepython" in self.config[section]:
                bp = self.config[section]["basepython"]
                bp_set.add(bp)
        return list(bp_set)
