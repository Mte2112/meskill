import xarray as xr


class Tools:
    """
    Core class for 'meskill' (ModelE Skill Scorer) program
    """
    
    def __init__(self):
        pass
         
        
    # Filler to lay out format 
    def func1():
        """
        This is just a filler for now
        """
        return None
    
    
    def __repr__(self):
    
        """Function to output the characteristics of these Tools
        
        Args:
            None
        
        Returns:
            string: characteristics of the tools
        
        """
        
        return "get_sample(direc, outdir), check_dim(ds), getstats(ds3, ds2, varexist)".\
        format(self.get_sample, self.check_dim, self.getstats)
    
    if __name__ == '__main__':
        sys.exit(main())  # next section explains the use of sys.exit