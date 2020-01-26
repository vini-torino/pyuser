import user, sys, getopt, utils, os, crypt
from getpass import getpass

utils.is_root()


argv = sys.argv[1:]
opts, argument = getopt.getopt(argv, ":c:d:g:G:k:p:s:h:u:" )

username = str(argument[0])
gid =  default_gid = user.group
gid_flag = False
shell = default_shell = user.shell
home = default_home = user.home + '/' + username
skel = default_skel = user.skel
uid = default_uid = user.group
uid_flag = False
gen_pass = True
password = 'x'
hashed_pass = user.password
comment = username

for opt, arg in opts:
    if  opt in ['-c']:
        comment = arg
    elif  opt in ['-d']:
        home = arg
    elif  opt in ['-g']:
        try:
            gid = utils.grep(user.group_file, arg)[0][1]
            gid_flag = True
        except IndexError as err:
            if gid is None:
                print(err, file=sys.stderr)
                sys.exit()
        except:
            gid_flag = False
    elif  opt in ['-G']:
        groups = arg.split(',')
    elif  opt in ['-k']:
        skel  = arg
    elif  opt in ['-p']:
        hashed_pass = arg
        gen_pass = False
    elif  opt in ['-h']:
        utils.call_help()
    elif  opt in ['-s']:
        shell = arg
    elif  opt in ['-u']:
          uid = arg
          uid_flag = True 

if username in user.all_users:
    print('user already exists!', file=sys.stderr)
    sys.exit()
elif uid in user.all_uids and uid_flag is True:
    print('uid has alredy been used!', file=sys.stderr)
    sys.exit()

if uid_flag is False:
    for i in range(user.uid_min , user.uid_max):
        if i not in user.all_uids:
            uid = i
            break

if user.is_usegroups_enabled == 'yes' and gid_flag is False:
    if not uid in user.all_gids:
        gid = uid
        group_tupple = (username, 'x', str(uid), '')
        group_string = ':'.join(group_tupple)
    else:
        for i in range(user.gid_min, user.gid_max):
            if i not in user.all_gids:
                gid = i
                group_tupple = (username, 'x', str(gid), '')
                group_string = ':'.join(group_tupple)
                break

if not gid_flag:
    with open('/etc/group', 'a') as f:
        f.writelines(group_string + '\n')
        f.close()


home = utils.check_dir(home, default_home)
skel = utils.check_dir(skel, default_skel)
shell = utils.check_file(shell, default_shell)

passwd_tuple = (username, password, str(uid), str(gid), comment, home ,shell )
passwd_string = ':'.join(passwd_tuple)


if gen_pass:
    pass1 = getpass('Type new unix password: ')
    pass2 = getpass('Retype new unix password: ')
    if pass1 == pass2:
        hashed_pass = crypt.crypt(pass1, crypt.mksalt(crypt.METHOD_SHA512))

shadow_tuple = (username, hashed_pass, user.epoch, user.pass_min_days, user.pass_max_days, user.pass_warn_age, user.inactive, user.reserved)
shadow_string = ':'.join(shadow_tuple)

with open('/etc/passwd', 'a') as f:
    f.write(passwd_string + '\n')
    f.close()

with open('/etc/shadow', 'a') as f:
    f.write(shadow_string + '\n')
    f.close()
