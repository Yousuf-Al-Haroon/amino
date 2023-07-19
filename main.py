from welcome import on_group_member_join
from goodbye import on_group_member_leave

from login import login

client = login()

@client.event("on_group_member_join")
def join(data): on_group_member_join(data)

@client.event("on_group_member_leave")
def leave(data): on_group_member_leave(data)

client.launch()