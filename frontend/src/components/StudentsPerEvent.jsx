import React, { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";
import { fetchAnalytics } from "../api/api"; // Make sure this points to your real API

export default function StudentsPerEvent() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      try {
        const analytics = await fetchAnalytics();

        // Ensure students_per_event is always an array
        const chartData = (analytics.students_per_event || []).map(event => ({
          name: `Event ${event.event_id}`,
          students: event.total || 0
        }));

        setData(chartData);
      } catch (err) {
        console.error("Error fetching analytics:", err);
        setData([]);
      } finally {
        setLoading(false);
      }
    }

    load();
  }, []);

  if (loading) return <p>Loading chart...</p>;
  if (!data.length) return <p>No data available</p>;

  return (
    <div style={{ width: "100%", height: 300, marginBottom: "50px" }}>
      <h2>Students per Event</h2>
      <ResponsiveContainer width="100%" height="100%">
        <BarChart data={data} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="name" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Bar dataKey="students" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
