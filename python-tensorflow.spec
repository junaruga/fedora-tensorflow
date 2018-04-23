# Created by pyp2rpm-3.3.2
%global pypi_name tensorflow

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        1%{?dist}
Summary:        TensorFlow helps the tensors flow

License:        Apache 2.0
URL:            https://www.tensorflow.org/
Source0:        https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}-cp33-cp33m-macosx_10_11_x86_64.whl
 
BuildRequires:  python3-devel
BuildRequires:  python3dist(absl-py) >= 0.1.6
BuildRequires:  python3dist(astor) >= 0.6.0
BuildRequires:  python3dist(gast) >= 0.2.0
BuildRequires:  python3dist(grpcio) >= 1.8.6
BuildRequires:  python3dist(numpy) >= 1.13.3
BuildRequires:  python3dist(protobuf) >= 3.4.0
BuildRequires:  python3dist(scipy) >= 0.15.1
BuildRequires:  python3dist(six) >= 1.10.0
BuildRequires:  python3dist(tensorboard) < 1.8.0
BuildRequires:  python3dist(tensorboard) >= 1.7.0
BuildRequires:  python3dist(termcolor) >= 1.1.0
BuildRequires:  python3dist(wheel) >= 0.26
BuildRequires:  python3dist(absl-py) >= 0.1.6
BuildRequires:  python3dist(astor) >= 0.6.0
BuildRequires:  python3dist(gast) >= 0.2.0
BuildRequires:  python3dist(grpcio) >= 1.8.6
BuildRequires:  python3dist(numpy) >= 1.13.3
BuildRequires:  python3dist(protobuf) >= 3.4.0
BuildRequires:  python3dist(six) >= 1.10.0
BuildRequires:  python3dist(tensorboard) < 1.8.0
BuildRequires:  python3dist(tensorboard) >= 1.7.0
BuildRequires:  python3dist(termcolor) >= 1.1.0
BuildRequires:  python3dist(wheel) >= 0.26
BuildRequires:  python3dist(setuptools)

%description
UNKNOWN

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}
 
Requires:       python3dist(absl-py) >= 0.1.6
Requires:       python3dist(astor) >= 0.6.0
Requires:       python3dist(gast) >= 0.2.0
Requires:       python3dist(grpcio) >= 1.8.6
Requires:       python3dist(numpy) >= 1.13.3
Requires:       python3dist(protobuf) >= 3.4.0
Requires:       python3dist(six) >= 1.10.0
Requires:       python3dist(tensorboard) < 1.8.0
Requires:       python3dist(tensorboard) >= 1.7.0
Requires:       python3dist(termcolor) >= 1.1.0
Requires:       python3dist(wheel) >= 0.26
Requires:       python3dist(setuptools)
%description -n python3-%{pypi_name}
UNKNOWN


%prep
%autosetup -n %{pypi_name}-%{version}.d
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%{__python3} setup.py test

%files -n python3-%{pypi_name}
%doc DESCRIPTION.rst
%{python3_sitelib}/__pycache__/*
%{python3_sitelib}/tensorflow-1/7/0/data.py
%{python3_sitearch}/%{pypi_name}
%{python3_sitearch}/%{pypi_name}-%{version}-py?.?.egg-info

%changelog
* Mon Apr 23 2018 Jun Aruga <jaruga@redhat.com> - 1.7.0-1
- Initial package.
