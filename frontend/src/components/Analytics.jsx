import React from "react";
import studentsperevent from "./studentsperevent";
import BuddyPairs from "./BuddyPairs";
import TopInterests from "./TopInterests";

export default function srcAnalytics() {
  return (
    <div style={{ padding: "20px" }}>
      <h1>Event srcAnalytics Dashboard</h1>
      <studentsperevent />
      <BuddyPairs />
      <TopInterests />
    </div>
  );
}
