def run_agent(command: str, agent_name: str = "general_agent") -> str:
    command_lower = command.lower()

    if "金融" in command or "市场" in command or "股市" in command:
        return f"[{agent_name}] 已完成金融市场初步分析任务：建议补充行情源、宏观新闻和资产清单。原始命令：{command}"

    if "写" in command or "文章" in command or "报告" in command:
        return f"[{agent_name}] 已生成写作任务草稿：主题已识别，下一步可扩展为自动成文。原始命令：{command}"

    if "客户" in command or "销售" in command:
        return f"[{agent_name}] 已生成销售跟进建议：建议建立潜在客户名单、需求分类和触达节奏。原始命令：{command}"

    return f"[{agent_name}] 已接收并处理任务。原始命令：{command}"
