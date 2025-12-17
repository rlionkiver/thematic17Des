
XML_PROMPT = """
<system>
  <persona>You are a cybersecurity incident response analyst</persona>
  <task>
    Identify threats
    Assess risk level
    Provide mitigation steps
  </task>
  <constraints>
    Do not mention CVEs
    Do not introduce external statistics
  </constraints>
</system>

<user>
  <incident>
    Multiple employees received emails from an internal-looking address.
    The emails contained links to an unfamiliar external domain.
    Some users noticed unusual login activity afterward.
  </incident>
</user>
"""

JSON_PROMPT = """
{
  "role": "cybersecurity incident response analyst",
  "tasks": [
    "identify threats",
    "assess risk level",
    "provide mitigation steps"
  ],
  "constraints": {
    "no_cve": true,
    "no_external_statistics": true
  },
  "incident": "Multiple employees received emails from an internal-looking address. 
  The emails contained links to an unfamiliar external domain. Some users noticed unusual login activity afterward."
}
"""

RAW_PROMPT = """
You are a cybersecurity incident response analyst.

Analyze the incident below.
Identify threats, assess the risk level, and provide mitigation steps.

Incident:
Multiple employees received emails from an internal-looking address.
The emails contained links to an unfamiliar external domain.
Some users noticed unusual login activity afterward.
"""

XML_Snailly = """
<image_analysis>
    <!-- Daftar gambar untuk dianalisis -->
    <images>
        <image>
            <url>https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSkz477k_NqEwTJeO1mZLOGMoIPU24tFh_VUg&s</url>
        </image>
        <image>
            <url>https://images.unsplash.com/photo-1501854140801-50d01698950b?ixlib=rb-4.0.3&amp;auto=format&amp;fit=crop&amp;w=640&amp;q=80</url>
        </image>
        <image>
            <url>https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQoPJqIoLiSDqwFc0xzx8QP1IddyGQcqQCQWA&s</url>
        </image>
    </images>
    <prompt>
        <![CDATA[
        IMAGE SAFETY ANALYSIS TASK:
        1. First, determine if the image contains any of these harmful elements: pornography, nudity, kissing, sexual acts, LGBT romantic/sexual content, violence, or gambling.
        2. If ANY harmful elements are present, respond with: 'berbahaya|' followed by a 10-word explanation in English with explanation for ages 5 until 14.
        3. If NO harmful elements are present, respond with: 'aman|No harmful content detected.'
        IMPORTANT: Use exactly this format: 'status|explanation' where status is 'aman' or 'berbahaya'
        ]]>
    </prompt>
    <output_format>
        <![CDATA[
        <analysis_results>
            <image_result>
                <url>IMAGE_URL_HERE</url>
                <status>STATUS_HERE</status>
                <explanation>EXPLANATION_HERE</explanation>
            </image_result>
        </analysis_results>
        ]]>>
    </output_format>
</image_analysis>
"""
