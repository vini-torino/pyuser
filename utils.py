import sys , getpass, os

def is_root():
    if getpass.getuser() != 'root':
        print('please, run this program as root', file=sys.stderr )
        sys.exit()

def check_dir(path, alternative):
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
            return(path)
        except:
            os.mkdir(alternative)
            print('Non fatal error: Invalid path ' + path, file=sys.stderr)
            return(alternative)
    else:
        return(path)

def check_file(path, alternative):
    if os.path.isfile(path):
        return(path)
    else:
            print('Non fatal error: Invalid file ' + path, file=sys.stderr)
            return(alternative)


def cat(path):
    data = []
    with open(path, 'r') as f:
        lines  = f.readlines()
        f.close()
        for line in lines:
            data.append(line.rstrip().split(':')) 
    return(data)


def grep(data, string):
    grepped = []
    for line in data:
        if string in line:
            grepped.append(line)
    return grepped


def cut(line):
    return line[0][1]


def gen_groups(data):
    groups = []
    for line in data:
        groups.append([ line[0], line[2] ] )
    return groups


def call_help():
    help_menu = """
    NAME
       setuser.py - create a new user or update default new user information

    SYNOPSIS
       setuser.py [options] LOGIN

       setuser.py -D

       setuser.py -D [options]

    DESCRIPTION
       setuser.py is a high level tool that  shows how  utilities like useradd works.

       When invoked without the -D option, the setuser.py creates a
       new user account using the values specified on the command line
plus the default values on our local files -  defaults and login.defs.

    OPTIONS
       The options which apply to the setuser.py command are:

        -D
           It will grep all values in defaults file.
    
        -e
           The date on which the user account will be disabled. The date
           is specified in the format YYYY-MM-DD.

           If not specified, useradd will use the default expiry date
           specified by the EXPIRE variable in defaults, or an
           empty string (no expiry) by default.
    
        -g
           The group name or number of the user's initial login group. The
           group name must exist. A group number must refer to an already
           existing group.
        
        -u
           The numerical value of the user's ID. This value must be
           unique, unless the -o option is used. The value must be
           non-negative. The default is to use the smallest ID value
           greater than or equal to UID_MIN and greater than every other
           user.

        -s
           The name of a new user's login shell.
            This option sets the SHELL variable in defaults

        -d
           The new user will be created using HOME_DIR as the value for
           the user's login directory. The default is to append the LOGIN
           name to BASE_DIR and use that as the login directory name. The
           directory HOME_DIR does not have to exist but will not be
           created if it is missing.

        -c
           Any text string. It is generally a short description of the
           login, and is currently used as the field for the user's full
           name.

        -G GROUP1[,GROUP2,...[,GROUPN]]]
           A list of supplementary groups which the user is also a member
           of. Each group is separated from the next by a comma, with no
           intervening whitespace. The groups are subject to the same
           restrictions as the group given with the -g option. The default
           is for the user to belong only to the initial group.

        -k SKEL_DIR
           The skeleton directory, which contains files and directories to
           be copied in the user's home directory, when the home directory
           is created by useradd.

           This option is only valid if the -m (or --create-home) option
           is specified.

           If this option is not set, the skeleton directory is defined by
           the SKEL variable in defaults  or, by default,
           /etc/skel.

        
        -m 
           Create the user's home directory if it does not exist. The
           files and directories contained in the skeleton directory
           (which can be defined with the -k option) will be copied to the
           home directory.

           By default, if this option is specified and CREATE_HOME is
           enabled, by default home directories are created.
        
        -M 
           Do no create the user's home directory, even if the system wide
           setting from login.defs (CREATE_HOME) is set to yes.
        
        -p SHA512_PASSWORD
           The encrypted password, as returned by crypt.crypt . The default is
           to disable the password.

        -f INACTIVE
           The number of days after a password expires until the account
           is permanently disabled. A value of 0 disables the account as
           soon as the password has expired, and a value of -1 disables
           the feature.
    """
    print(help_menu)

