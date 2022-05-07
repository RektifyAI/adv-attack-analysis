npm install beneath-react

import { useRecords } from "beneath-react";

const App = () => {
  const { records, loading, error } = useRecords({
    table: "bubblyorca/seal-dataset/attack-data",
    // Other useful options:
    // secret: "INSERT",
    // query: { type: "log", peek: false },
    // query: { type: "index", filter: 'FILTER' },
    // subscribe: true,
  })

  if (loading) {
    return <p>Loading...</p>;
  } else if (error) {
    return <p>Error: {error}</p>;
  }

  return (
    <div>
      <h1>attack-data</h1>
      <ul>
        {records.map((record) => (
          <li key={record["@meta"].key}>
            {JSON.stringify(record)}
          </li>
        ))}
      </ul>
    </div>
  );
}
