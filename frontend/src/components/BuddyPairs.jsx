import React, { useEffect, useState } from "react";
import { PieChart, Pie, Cell, Tooltip, ResponsiveContainer } from "recharts";
import { fetchAnalytics } from "../api/api";

const COLORS = ["#0088FE", "#00C49F"];

export default function BuddyPairs() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function load() {
      const analytics = await fetchAnalytics();
      const chartData = analytics.buddy_pairs_per_event.map(bp => {
        const total = analytics.students_per_event.find(e => e.event_id === bp.event_id)?.total || 0;
        return { name: `Event ${bp.event_id}`, paired: bp.paired_students, unpaired: total - bp.paired_students };
      });
      setData(chartData);
      setLoading(false);
    }
    load();
  }, []);

  if (loading) return <p>Loading chart...</p>;
  if (!data.length) return <p>No data available</p>;

  return (
    <div style={{ margin: "20px 0" }}>
      <h2>Buddy Match Distribution</h2>
      {data.map((event, i) => (
        <div key={i}>
          <h3>{event.name}</h3>
          <ResponsiveContainer width="100%" height={200}>
            <PieChart>
              <Pie
                data={[
                  { name: "Paired", value: event.paired },
                  { name: "Unpaired", value: event.unpaired }
                ]}
                dataKey="value"
                nameKey="name"
                outerRadius={80}
                label
              >
                {[
                  { name: "Paired", value: event.paired },
                  { name: "Unpaired", value: event.unpaired }
                ].map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      ))}
    </div>
  );
}
