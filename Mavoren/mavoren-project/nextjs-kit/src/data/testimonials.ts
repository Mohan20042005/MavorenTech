export interface Testimonial { text: string; name: string; business: string; location: string; rating: 1 | 2 | 3 | 4 | 5 }

// Add only real feedback a client has given you, with their permission to quote it.
// The testimonials section renders only when this list is not empty.
export const testimonials: Testimonial[] = []
