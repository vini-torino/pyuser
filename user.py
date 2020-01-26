from utils import cat, cut, grep , gen_groups, is_root
from time import time

is_root()

group_file = gen_groups(cat('/etc/group'))
shadow_file = cat('/etc/shadow')
passwd_file = gen_groups(cat('/etc/passwd'))


all_users = []
all_uids = []
all_groups = []
all_gids = [] 


for user in passwd_file:
    all_users.append(user[0])
    all_uids.append(int(user[1]))

for group in group_file:
    all_groups.append(group[0])
    all_gids.append(int(group[1]))
    

defaults = cat('defaults')
home = cut(grep(defaults, 'HOME'))
shell = cut(grep(defaults, 'SHELL'))
group = cut(grep(defaults, 'GROUP'))
skel = cut(grep(defaults, 'SKEL'))
del(defaults)

login_defs = cat('login.defs')
pass_max_days = cut(grep(login_defs, 'PASS_MAX_DAYS'))
pass_min_days = cut(grep(login_defs, 'PASS_MIN_DAYS'))
pass_warn_age =  cut(grep(login_defs, 'PASS_WARN_AGE'))
uid_min = int(cut(grep(login_defs, 'UID_MIN')))
uid_max = int(cut(grep(login_defs, 'UID_MAX')))
gid_min = int(cut(grep(login_defs, 'GID_MIN')))
gid_max = int(cut(grep(login_defs, 'GID_MAX')))
is_home_needed = cut(grep(login_defs, 'CREATE_HOME'))
is_usegroups_enabled =  cut(grep(login_defs, 'USERGROUPS_ENAB'))
encrypt_method = cut(grep(login_defs, 'ENCRYPT_METHOD'))
del(login_defs)

password = '!'
epoch = str(int(((((time())/ 60) / 60 )/24)))
inactive = ''
reserved = ''