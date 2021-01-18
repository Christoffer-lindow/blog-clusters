import React, { useState } from "react";
import {
  Box,
  Button,
  Heading,
  Input,
  InputGroup,
  VStack,
  HStack,
  Link,
  FormControl,
  FormLabel,
  Spinner
} from "@chakra-ui/react";
import { Link as RouterLink } from "react-router-dom";
import axios from "axios";
import DataTabs from "../components/DataTabs";

const ClusterPage = () => {
  const [queryResults, setQueryResults] = useState([]);
  const [queryTime, setQueryTime] = useState(null);
  const [k, setK] = useState(5);
  const [n, setN] = useState(20);
  const [loading,setLoading] = useState(false)

  const handleKChange = (e) => {
    setK(e.target.value);
  };

  const handleNChange = (e) => {
    setN(e.target.value);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    console.log("we got here");
    const qString = `http://127.0.0.1:8000/k-means/${k}/${n}`;
    setLoading(true)
    const result = await axios.get(qString);
    const { data } = result;
    setQueryResults(data.centroids);
    setQueryTime(data.runtime);
    setLoading(false)
  };
  return (
    <>
      <VStack spacing={4} align="stretch">
        <Box>
          <Heading marginBottom="4">Blog clusterer</Heading>
        </Box>
        <Box>
          <p>
            The clusters were made from a blog dataset consisting of words and
            number of words at a given index in the dataset
          </p>
          <p>To generate the clusters k-means were used.</p>
          <p>
            For more information about the project check the{" "}
            <Link as={RouterLink} to="/about" fontWeight="bold">
              About page
            </Link>
          </p>
        </Box>
        <Box>
          <FormControl onSubmit={(e) => handleKChange(e)}>
            <HStack spacing={5}>
              <InputGroup>
                <FormLabel htmlFor="k" paddingTop="1">
                  Clusters
                </FormLabel>
                <Input
                  id="k"
                  placeholder="Enter number of clusters"
                  value={k}
                  onChange={handleKChange}
                />
              </InputGroup>
              <FormLabel htmlFor="n">Itterations</FormLabel>
              <Input
                id="n"
                placeholder="Enter number of itterations"
                value={n}
                onChange={handleNChange}
              />
              <Button
                paddingLeft="7"
                paddingRight="7"
                type="submit"
                onClick={(e) => handleSubmit(e)}
              >
                Run
              </Button>
            </HStack>
          </FormControl>
        </Box>
        {loading ? <Spinner size="lg"/> : (
        <DataTabs clusters={queryResults} runtime={queryTime}></DataTabs>
        )}
      </VStack>
    </>
  );
};

export default ClusterPage;
