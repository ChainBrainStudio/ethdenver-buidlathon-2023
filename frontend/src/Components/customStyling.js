import styled from "@emotion/styled";
import { Select } from "@mui/material";

export const StyledSelect = styled(Select)`
  height: 45px;
  width: 100%;
  color: white;
  & .MuiOutlinedInput-notchedOutline {
    border-color: white
  };
  &.Mui-focused .MuiOutlinedInput-notchedOutline {
    border-color: white
  };
  &:hover .MuiOutlinedInput-notchedOutline {
    border-color: white;
    border-width: 2px
  };
  // & > fieldset {
  //   border-color: white;
  // };
  & > svg {
    color: white;
  }
  `;

// export const useStyles = makeStyles(theme => ({
//     root: {
//       width: "100%"
//     },
//     paper: {
//       marginTop: theme.spacing(3),
//       width: "100%",
//       overflowX: "auto",
//       marginBottom: theme.spacing(2),
//       margin: "auto"
//     },
//     table: {
//       width: '100%',
//     }
//   }));