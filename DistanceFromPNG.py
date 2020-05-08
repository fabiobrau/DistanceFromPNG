#!/usr/bin/env python3
import argparse

def main_process():
    parser = argparse.ArgumentParser()
    parser.add_argument('pics',
                        type=str,
                        nargs='+',
                        metavar='Pic1 Pic2',
                        help='''List of Pictures'''
                       )
    parser.add_argument('-f', '--focal-length',
                        type=float,
                        nargs='+',
                        dest='focals',
                        help='''List of relative focal length for each picture'''
                       )
    parser.add_argument('-d', '--distance',
                        type=float,
                        nargs='+',
                        dest='distances',
                        help='''List of relative distance from each picture and
                        the first one.'''
                       )

if __name__=='__main__':
    main_process()
