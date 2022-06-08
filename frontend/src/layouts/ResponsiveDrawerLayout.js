import React from 'react';
import { useState } from 'react';
import { 
    Box,
    Typography,
    } from '@mui/material';
import CustomAppBar from '../components/appBar/AppBar';



const ResponsiveDrawerLayout = () => {
    // state
    const [mobileOpen, setMobileOpen] = useState(false);
    // useEffect

    // constants
    const drawerWidth = 300;
    
    return (
        <Box sx = {{display: 'flex' }}>
            <CustomAppBar />

        </Box>
    );
};

export default ResponsiveDrawerLayout;