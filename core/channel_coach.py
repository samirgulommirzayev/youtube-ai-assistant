"""
Kanalni 0 dan monetizatsiyaga olib chiqish uchun yo'l xaritasi va maslahat.
"""
from core.ai_client import ask_ai

SYSTEM_BASE = """You are a YouTube growth strategist who has taken multiple channels
from 0 subscribers to full monetization, with deep expertise in the American audience
and YouTube Shorts algorithm. You give specific, actionable advice — never generic
fluff like "be consistent" without concrete numbers and steps."""


def build_growth_roadmap(niche: str, current_subs: int, current_status: str) -> str:
    prompt = f"""Niche: {niche}
Current subscriber count: {current_subs}
Current situation: {current_status}

Build a step-by-step roadmap to reach YouTube Partner Program monetization
(1,000 subs + 10M Shorts views in 90 days, OR 1,000 subs + 4,000 watch hours in 12 months).

Include:
1. Posting frequency and best content format for this niche right now
2. Milestones (0-100, 100-500, 500-1000 subs) with what changes at each stage
3. Common mistakes that stall growth at this niche/stage
4. What to track weekly to know if it's working"""
    return ask_ai(SYSTEM_BASE, prompt)


def analyze_channel_gap(channel_description: str) -> str:
    """
    Foydalanuvchi kanal linkini yoki tavsifini yuborganda (avtomatik API
    ulanmagunча), qo'lda kiritilgan ma'lumot asosida tahlil beradi.
    """
    prompt = f"""Here is information about a YouTube channel:

{channel_description}

Analyze this channel and tell me:
1. What's working
2. What's the single biggest thing holding it back from growth
3. 3 specific changes to make this week"""
    return ask_ai(SYSTEM_BASE, prompt)
