SAFE_ACTIONS={"open_palm":"pause","thumbs_up":"confirm","thumbs_down":"cancel","peace":"next","fist":"stop"}
def action_for(label): return SAFE_ACTIONS.get(label)
# Keep automation disabled until explicit confirmation and safety testing.
