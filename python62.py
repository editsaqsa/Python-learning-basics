# dictionary methods
bot_setting = {
    "bot_name": "bot alpha",
    "status": "testing",
    "risk_level": "low",
}
bot_setting.update({"status": "live", "monthly_target": "5%"})
print("update k bad bot setting:",bot_setting)
bot_setting.pop("risk_level")
print("after popping risk_level:",bot_setting)
