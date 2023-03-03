import * as React from 'react';
import Paper from '@mui/material/Paper';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import { connect } from 'react-redux';
import { CircularProgress } from '@mui/material';
import {humanize as h} from "@jsdevtools/humanize-anything"
import humanize from 'humanize-plus';
;


function buildColumns(data){
    let column_header = Object.keys(data[0]);
    var columns = []

    for (var index = 0; index < column_header.length; index++)
    {   
        columns.push({id: column_header[index], label: column_header[index], minWidth: 170, align: "center",format: (value) => {
          if(typeof(value) == "number"){
            return humanize.formatNumber(value, 2)
          }
          else{

          return h(value)} }})

    }

    
    return columns
    
}

export function StickyHeadTable(props) {
    
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
//   console.log(props.data);
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };

  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };
  let columns = props.data ? buildColumns(props?.data) : [];
  if(props.isLoading){
    return (
      <CircularProgress sx={{ align: 'center', marginTop:"10px",} }  color="secondary"/>
  )}
  else{
    let rows = props.data? props.data: []; 


  return (
    props.data && (
    <Paper sx={{ width: '80%', overflow: 'hidden', align: 'center', marginTop:"10px"}}>
      <TableContainer sx={{ maxHeight: 440 }}>
        <Table stickyHeader aria-label="sticky table">
          <TableHead >
            <TableRow >
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                  sx={{textAlign: 'center', backgroundColor: '#494F55', color:'white', fontWeight: "bold"}}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows
              .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
              .map((row) => {
                return (
                  <TableRow hover role="checkbox" tabIndex={-1} key={row.id}>
                    {columns.map((column) => {
                      const value = row[column.id];
                      return (
                        <TableCell key={column.id} align={column.align} sx={{textAlign: 'center'}}>
                          {column.format && typeof value === 'number'
                            ? column.format(value)
                            : value}
                        </TableCell>
                      );
                    })}
                  </TableRow>
                );
              })}
          </TableBody>
        </Table>
      </TableContainer>
      <TablePagination
        rowsPerPageOptions={[10, 25, 100]}
        component="div"
        count={rows.length}
        rowsPerPage={rowsPerPage}
        page={page}
        onPageChange={handleChangePage}
        onRowsPerPageChange={handleChangeRowsPerPage}
      />
    </Paper>
  ));
}}

const mapStateToProps = state => {
    return {
      data: state.counter.data,
      isLoading: state.counter.isLoading
    }
  }

export default connect(mapStateToProps)(StickyHeadTable)