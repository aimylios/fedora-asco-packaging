Name:           asco
Version:        0.4.10
Release:        1%{?dist}
Summary:        A SPICE Circuit Optimizer

License:        GPLv2
URL:            http://asco.sourceforge.net/index.html

Source:         https://datapacket.dl.sourceforge.net/project/asco/asco/0.4.10/ASCO-%{version}.tar.gz

BuildRequires:  gcc

%define debug_package %{nil}

%description
ASCO project aims to bring circuit optimization capabilities to existing SPICE
simulators using a high-performance parallel differential evolution (DE)
optimization algorithm. Currently out-of-the-box support for Eldo, HSPICE,
LTspice, Spectre, Qucs and ngspice exist. 

%prep
%setup -q -n ASCO-%{version}

%build
%make_build

%install
%{__mkdir} -p %{buildroot}%{_bindir}
%{__cp} -p asco %{buildroot}%{_bindir}
%{__cp} -p asco-test %{buildroot}%{_bindir}
%{__mkdir} -p %{buildroot}%{_datadir}/%{name}
%{__cp} -p -r examples %{buildroot}%{_datadir}/%{name}
%{__mkdir} -p %{buildroot}%{_datadir}/%{name}/tools
%{__cp} -p tools/alter/alter %{buildroot}%{_datadir}/%{name}/tools
%{__cp} -p tools/log/log %{buildroot}%{_datadir}/%{name}/tools
%{__cp} -p tools/monte/monte %{buildroot}%{_datadir}/%{name}/tools
%{__cp} -p tools/postp/postp %{buildroot}%{_datadir}/%{name}/tools

%files
%{_bindir}/asco*
%{_datadir}/%{name}/examples/*
%{_datadir}/%{name}/tools/*
%doc doc/ASCO.pdf 
%license LICENSE

%changelog
* Sat Jul 28 2018 Aimylios <aimylios@xxx.xx> - 0.4.10-1
- Initial release
