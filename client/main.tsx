import React, { useState } from 'react';
import { useQuery } from '@apollo/client';
import { gql } from '@apollo/client';
import LifecycleView from '../components/LifecycleView';
import DetailsView from '../components/DetailsView';
import TextView from '../components/TextView';
import SchemaView from '../components/SchemaView';
import DataEditView from '../components/DataEditView';
import ErrorBoundary from '../components/ErrorBoundary';
import LoadingSpinner from '../components/LoadingSpinner';

const GET_LIFECYCLE_DATA = gql`
  query GetLifecycleData {
    stages {
      id
      stage
      substages {
        id
        substagename
      }
    }
    connections {
      start
      end
      type
    }
  }
`;

interface Stage {
  id: string;
  stage: string;
  substages: { id: string; substagename: string }[];
}

interface Connection {
  start: string;
  end: string;
  type: string;
}

interface LifecycleData {
  stages: Stage[];
  connections: Connection[];
}

const tabs = ['Lifecycle', 'Details', 'Text', 'Schema', 'Edit Data'] as const;
type TabType = typeof tabs[number];

export default function Home() {
  const [selectedTab, setSelectedTab] = useState<TabType>('Lifecycle');
  const { loading, error, data } = useQuery<LifecycleData>(GET_LIFECYCLE_DATA);

  const renderContent = () => {
    if (loading) return <LoadingSpinner />;
    if (error) return <p>Error: {error.message}</p>;
    if (!data) return <p>No data available</p>;

    switch (selectedTab) {
      case 'Lifecycle':
        return <LifecycleView stages={data.stages} connections={data.connections} />;
      case 'Details':
        return <DetailsView />;
      case 'Text':
        return <TextView />;
      case 'Schema':
        return <SchemaView />;
      case 'Edit Data':
        return <DataEditView stages={data.stages} />;
      default:
        return null;
    }
  };

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Research Data Lifecycle Visualization</h1>
      <div className="flex">
        <div className="w-1/4 pr-4">
          <h2 className="text-xl font-semibold mb-2">Select View:</h2>
          {tabs.map((tab) => (
            <button
              key={tab}
              className={`block w-full text-left p-2 mb-2 ${
                selectedTab === tab ? 'bg-blue-500 text-white' : 'bg-gray-200'
              }`}
              onClick={() => setSelectedTab(tab)}
            >
              {tab}
            </button>
          ))}
        </div>
        <div className="w-3/4">
          <ErrorBoundary>
            {renderContent()}
          </ErrorBoundary>
        </div>
      </div>
    </div>
  );
}
