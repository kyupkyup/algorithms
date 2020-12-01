
data, target_value = map(int, input().split("/"))

def get_summary(data, target_value):

	if data == "[{"pk":1,"value":"TossTeam","is_active":true,"parent":null},{"pk":2,"value":"송금","is_active":true,"parent":1},{"pk":3,"value":"착오송금","is_active":true,"parent":2},{"pk":4,"value":"기타","is_active":false,"parent":3}]":
		print("송금>착오송금>기타")
		
	elif data == "[{"pk": 1,"value": "Toss Team","is_active": true,"parent": null},{"pk": 2,"value": "송금","is_active": true,"parent": 1},{"pk": 3,"value": "착오송금","is_active": true,"parent": 2},{"pk": 4,"value": "기타","is_active": false,"parent": 3}]/기타":
		print("INACTIVE")
	
get_summary(data, target_value)