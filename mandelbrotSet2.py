import numpy as np
import matplotlib.pyplot as plt

def mandelbrot(h, w, max_iter):
    """
    Generate a Mandelbrot set image of dimensions (h, w).
    
    Parameters:
    h, w (int): Height and width of the output image
    max_iter (int): Maximum number of iterations to determine if a point escapes
    
    Returns:
    numpy.ndarray: 2D array of iteration counts for each point
    """
    # Define the region of the complex plane to investigate
    y, x = np.ogrid[-1.4:1.4:h*1j, -2:0.8:w*1j]
    c = x + y*1j  # Create a complex plane
    z = c.copy()  # Start with z = c
    
    # Initialize the result array for iteration counts
    result = np.zeros(z.shape, dtype=int)
    
    # For each pixel, determine how quickly the value escapes to infinity
    for i in range(max_iter):
        # Only compute for points that haven't escaped yet
        mask = np.abs(z) < 2.0
        
        # Update: z = z² + c
        z[mask] = z[mask]**2 + c[mask]
        
        # Count iterations for points that are still within the threshold
        result[mask] += 1
    
    return result

def plot_mandelbrot(h=1000, w=1500, max_iter=100, cmap='hot'):
    """
    Create and display a Mandelbrot set plot.
    
    Parameters:
    h, w (int): Height and width of the output image
    max_iter (int): Maximum number of iterations for the Mandelbrot computation
    cmap (str): Matplotlib colormap name
    """
    # Compute the Mandelbrot set
    mandelbrot_set = mandelbrot(h, w, max_iter)
    
    # Create the figure and plot
    plt.figure(figsize=(12, 8))
    plt.imshow(mandelbrot_set, cmap=cmap, origin='lower')
    plt.title(f'Mandelbrot Set (max iterations: {max_iter})')
    plt.tight_layout()
    plt.axis('off')  # Hide axes
    plt.colorbar(label='Iteration count')
    plt.show()

# Generate and display the Mandelbrot set
plot_mandelbrot(max_iter=100)

# Optional: Save the plot to a file
# plt.savefig('mandelbrot.png', dpi=300, bbox_inches='tight')
