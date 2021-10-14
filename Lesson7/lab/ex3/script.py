#!/usr/bin/env python
from __future__ import print_function, absolute_import, division

import logging
import mysql.connector

from stat import S_IFDIR, S_IFREG
from time import time

from fuse import FUSE, FuseOSError, Operations, LoggingMixIn, fuse_get_context


class Context(LoggingMixIn, Operations):
    'Example filesystem to demonstrate fuse_get_context()'

    def getattr(self, path, fh=None):
        if path == "/":
            st = dict(st_mode=(S_IFDIR | 0o755), st_nlink=2)
        else:
            filename = path[1:]  # Remove leading /


            if filename == '' or filename is None:
                raise FuseOSError("ENOENT")


            st = dict(st_mode=(S_IFREG | 0o755), st_size=filesize)

        st['st_ctime'] = st['st_mtime'] = st['st_atime'] = time()
        return st

    def read(self, path, size, offset, fh):

        def encoded(x):
            return ('%s\n' % x).encode('utf-8')

        filename = path[1:]
        if filename == '' or filename is None:
            raise FuseOSError("ENOENT")

        c = db.cursor(prepared=True)
        c.execute("SELECT * FROM Files WHERE filename = %s", (filename))

        return self

        # TODO: if filename does not exist, raise: raise FuseOSError(ENOENT)
        # If filename exists, return file content

    def readdir(self, path, fh):
        Files = []

        # TODO: Files should contain list of filenames in directory.     
        return ['.', '..'] + Files

    # Disable unused operations:
    access = None
    flush = None
    getxattr = None
    listxattr = None
    open = None
    opendir = None
    release = None
    releasedir = None
    statfs = None


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('mount')
    args = parser.parse_args()

    # TODO: Establish mysql connection
    db = mysql.connector.Connect(
        host="db",
        user="root",
        passwd="test",
        database="test"
    )

    db.cursor().execute("""
        CREATE TABLE IF NOT EXISTS Files (
            fileid INT AUTO_INCREMENT,
            filename VARCHAR(255),
            filesize INT,
            filecontent BLOB       
        );
    """)

    logging.basicConfig(level=logging.WARNING)
    fuse = FUSE(
        Context(c), args.mount, foreground=True, ro=True, allow_other=True)
