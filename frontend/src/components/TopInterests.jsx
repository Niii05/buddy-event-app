import React, { useEffect, useState } from "react";
import { BarChart, Bar, XAxis, YAxis, Tooltip, CartesianGrid, ResponsiveContainer } from "recharts";
import { fetchAnalytics } from "../api/api";

export default function TopInterests() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const analytics = await fetchAnalytics();
      const chartData = analytics.top_interests.map(([interest, count]) => ({ interest, count }));
      setData(chartData);
      setLoading(false);
    }
    load();
  }, []);

  if (loading) return <p>Loading chart...</p>;
  if (!data.length) return <p>No data available</p>;

  return (
    <div style={{ margin: "20px 0" }}>
      <h2>Top Interests</h2>
      <ResponsiveContainer width="100%" height={300}>
        <BarChart data={data} margin={{ top: 20, right: 30, left: 0, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="interest" />
          <YAxis allowDecimals={false} />
          <Tooltip />
          <Bar dataKey="count" fill="#82ca9d" />
        </BarChart>
      </ResponsiveContainer>
    </div>
  );
}
