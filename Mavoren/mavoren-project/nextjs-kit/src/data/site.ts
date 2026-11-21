export const site = {
  "name": "Mavoren",
  "headline": "Your Vision. Our Digital Craft.",
  "supporting": "Transforming Ideas Into Digital Excellence.",
  "email": "mavorentech@gmail.com",
  "phone": "+91 73391 32560",
  "whatsapp": "917339132560",
  "instagram": "https://www.instagram.com/mavoren_tech?jplx=N2Frb2swb3V2M3B0&utm_source=qr",
  "facebook": "https://www.facebook.com/share/16YNPCekdh8/?mibextid=wwXIfr",
  "areaServed": "Tamil Nadu, India",
  "technologies": [
    "HTML5",
    "CSS3",
    "JavaScript (ES6+)",
    "React.js",
    "Responsive Web Design",
    "Git & GitHub",
    "Figma",
    "Firebase",
    "Spring Boot"
  ]
} as const

export const offers = {
  "domain": {
    "title": "FREE DOMAIN ON BULK ORDERS!",
    "body": "Get a FREE Domain on eligible bulk website orders worth ₹15,000 or above.",
    "tagline": "More Projects. More Value. Your Domain Is On Us!",
    "terms": "Applicable to eligible bulk orders with a combined project value of ₹15,000 or above. Subject to domain availability and applicable terms."
  },
  "social": {
    "title": "10% off when you contact us from social media",
    "body": "Message Mavoren on Instagram or Facebook and get a 10% offer. Subject to applicable terms."
  }
} as const

export const waLink = (text: string) => `https://wa.me/${site.whatsapp}?text=${encodeURIComponent(text)}`
