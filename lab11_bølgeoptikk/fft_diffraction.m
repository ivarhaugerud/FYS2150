%Diffraction by FFT

%?yvind Gl?ersen, 11.10.13

%set up screen with slits
n = 1024;
screen = zeros(n); %generate a screen with 0 transparency
middle = n/2;
n_slits = 10; %number of slits
slit_width = 5; % width of one slit
slit_dist = 2*slit_width; %distance between slits
slit_length = 100; %make this an even number


%add slits to center of screen
first_slit =  middle-round(0.5*(n_slits*slit_dist-slit_dist));
for slit=1:n_slits
    slit_pos = (slit-1)*(slit_dist);
    screen(middle-slit_length/2:middle+slit_length/2,...
      (first_slit+slit_pos):(first_slit+slit_pos+slit_width-1)) = 1;  
end
%check that screen looks ok:
figure(1)
imagesc(screen), title 'Diffraction screen',axis equal
colormap(gray)
%% find diffraction pattern
pattern = abs(fft2(screen));
pattern = fftshift(pattern);
%view pattern
figure(2)
imagesc(pattern), title 'Diffraction pattern',axis equal
colormap(copper)




