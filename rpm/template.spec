Name:           ros-lunar-radar-omnipresense
Version:        0.0.1
Release:        1%{?dist}
Summary:        ROS radar_omnipresense package

Group:          Development/Libraries
License:        ECL2.0
URL:            http://www.ros.org/wiki/radar_omnipresense
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-message-generation
Requires:       ros-lunar-message-runtime
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-rospy
Requires:       ros-lunar-std-msgs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-message-generation
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-rospy
BuildRequires:  ros-lunar-std-msgs

%description
This is the radar driver package developed for the omnipresense radar module.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Sat Apr 07 2018 Garren Hendricks <ghendricks@scu.edu> - 0.0.1-1
- Autogenerated by Bloom

* Sat Apr 07 2018 Garren Hendricks <ghendricks@scu.edu> - 0.0.1-0
- Autogenerated by Bloom

