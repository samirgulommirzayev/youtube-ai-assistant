"""
Amerika auditoriyasi uchun video kontenti generatori:
- Ssenariy (script)
- Sarlavha (title)
- Teg va hashteglar
- Hook (birinchi 3 soniyalik jumla)
"""
from core.ai_client import ask_ai

SYSTEM_BASE = """You are an expert YouTube content strategist specializing in the American audience, particularly Shorts and viral short-form video content. You understand American internet culture, slang, pacing, and what makes American viewers stop scrolling. Always respond in English, since the content is for an American audience, unless explicitly asked otherwise."""


def generate_script(niche: str, topic: str, video_length_seconds: int = 30) -> str:
    prompt = f"""Niche: {niche}
Topic/idea: {topic}
Target length: {video_length_seconds} seconds

Write a YouTube Shorts script for an American audience. Structure:
1. HOOK (first 1-2 seconds, must stop scrolling)
2. BODY (fast-paced, retains attention, no dead air)
3. PAYOFF/ENDING (satisfying loop or cliffhanger to boost rewatch rate)

Include approximate timing for each beat."""
    return ask_ai(SYSTEM_BASE, prompt)


def generate_title_tags_hashtags(niche: str, topic: str) -> str:
    prompt = f"""Niche: {niche}
Topic/idea: {topic}

Give me:
1. 5 title options (under 60 characters, high CTR style, American Shorts audience)
2. 15 relevant tags (comma separated, mix of broad + specific)
3. 8 trending-style hashtags (include niche-specific + broad reach ones)

Format clearly with headers."""
    return ask_ai(SYSTEM_BASE, prompt)


def generate_hooks(niche: str, topic: str, count: int = 5) -> str:
    prompt = f"""Niche: {niche}
Topic/idea: {topic}

Give me {count} different hook options for the first 1-2 seconds of a Shorts video.
Each hook should use a different psychological trigger (curiosity gap, controversy,
relatable pain point, shocking stat, direct callout, etc). Label the trigger type
used for each one."""
    return ask_ai(SYSTEM_BASE, prompt)


def critique_video(description: str) -> str:
    """
    Foydalanuvchi video haqida yozma tavsif bersa (nima bo'layotgani,
    hozirgi hook, retention data bo'lsa), AI nima yetishmayotganini aytadi.
    """
    prompt = f"""Here is a description of my video and its performance:

{description}

Based on this, tell me:
1. What's likely hurting retention/watch time
2. What's missing (hook, pacing, payoff, captions, etc)
3. 3 concrete, specific fixes I can apply to my NEXT video"""
    return ask_ai(SYSTEM_BASE, prompt)
