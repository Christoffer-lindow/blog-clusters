import {
  Center,
  Tab,
  TabList,
  TabPanel,
  TabPanels,
  Tabs,
} from "@chakra-ui/react";
import React from "react";
import DataTable from "./DataTable";

const DataTabs = ({ clusters, runtime }) => {
  const formatDecimalts = (number) => {
    return Math.round((number + Number.EPSILON) * 1000) / 1000;
  };
  return (
    <Tabs isFitted variant="enclosed">
      <TabList mb="1em">
        {clusters.map((cluster, i) => (
          <Tab key={i + 1}>Cluster {i + 1}</Tab>
        ))}
      </TabList>
      <TabPanels>
        {clusters.map((cluster) => (
          <TabPanel>
            <DataTable blogs={cluster.blogs} />
            <Center>
              <p>Execution time: {formatDecimalts(runtime)} seconds</p>
            </Center>
          </TabPanel>
        ))}
      </TabPanels>
    </Tabs>
  );
};

export default DataTabs;
