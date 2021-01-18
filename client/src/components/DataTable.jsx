import { Table,Tbody, Td, Th, Thead, Tr } from "@chakra-ui/react";
import React from "react";

const DataTable = ({blogs}) => {
  return (
    <Table variant="simple" size="sm">
      <Thead>
        <Tr>
          <Th>Blog name</Th>
        </Tr>
      </Thead>
      <Tbody>
            {blogs.map(blog => (<Tr><Td>{blog}</Td></Tr>))}
      </Tbody>
    </Table>
  );
};

export default DataTable;
