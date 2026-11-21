import type { TierCard } from './types'

export const tiers: TierCard[] = [
  {
    "name": "Starter",
    "tagline": "Fast, focused sites to get you online.",
    "from": "₹2,999",
    "popular": false,
    "services": [
      {
        "label": "Landing Page",
        "serviceType": "Landing Pages",
        "price": "₹2,999",
        "description": "One focused page built around a single action."
      },
      {
        "label": "Website Redesign",
        "serviceType": "Website Redesign",
        "price": "₹3,999",
        "description": "A faster, mobile-friendly rebuild of your existing site."
      },
      {
        "label": "Portfolio Website",
        "serviceType": "Portfolio Websites",
        "price": "₹4,999",
        "description": "Showcase sites for creators, freelancers and studios."
      }
    ]
  },
  {
    "name": "Business",
    "tagline": "For businesses, institutions and clinics.",
    "from": "₹6,999",
    "popular": true,
    "services": [
      {
        "label": "Business Website",
        "serviceType": "Business Websites",
        "price": "₹6,999",
        "description": "Clear, credible company sites that turn visitors into enquiries."
      },
      {
        "label": "Restaurant / Cafe Website",
        "serviceType": "Restaurant & Cafe Websites",
        "price": "₹6,999",
        "description": "Menus, offers, reservations and directions in one place."
      },
      {
        "label": "Real Estate Website",
        "serviceType": "Real Estate Websites",
        "price": "₹9,999",
        "description": "Property presentation and enquiry flows."
      },
      {
        "label": "Educational Website",
        "serviceType": "Educational Websites",
        "price": "₹9,999",
        "description": "Course, admissions and information sites."
      },
      {
        "label": "Healthcare Website",
        "serviceType": "Healthcare Websites",
        "price": "₹9,999",
        "description": "Service and appointment information for clinics."
      }
    ]
  },
  {
    "name": "Premium",
    "tagline": "For online stores and custom builds.",
    "from": "₹14,999",
    "popular": false,
    "services": [
      {
        "label": "E-commerce Website",
        "serviceType": "E-commerce Websites",
        "price": "₹14,999",
        "description": "Online stores with product pages, carts and ordering flows."
      },
      {
        "label": "Custom Web Application",
        "serviceType": "Custom Web Applications",
        "price": "Custom quote",
        "description": "Tailored web apps built around your workflow."
      },
      {
        "label": "UI/UX Design",
        "serviceType": "UI/UX Design",
        "price": "Ask for a quote",
        "description": "Interface and experience design before development starts."
      }
    ]
  }
]
