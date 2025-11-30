export const API_BASE = "https://7j9aqutjt6.execute-api.ap-south-1.amazonaws.com/prod";

export async function fetchAnalytics() {
  const res = await fetch(`${API_BASE}/analytics`);
  if (!res.ok) throw new Error("Failed to fetch analytics data");
  return res.json();
}

export async function fetchEvents() {
  const res = await fetch(`${API_BASE}/events`);
  if (!res.ok) throw new Error("Failed to fetch events");
  return res.json();
}

export async function fetchRegistrations(eventId) {
  const res = await fetch(`${API_BASE}/registrations/${eventId}`);
  if (!res.ok) throw new Error(`Failed to fetch registrations for event ${eventId}`);
  return res.json();
}
