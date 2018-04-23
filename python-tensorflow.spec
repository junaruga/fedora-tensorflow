# Created by pyp2rpm-3.3.2
%global pypi_name tensorflow

Name:           python-%{pypi_name}
Version:        1.7.0
Release:        1%{?dist}
Summary:        TensorFlow helps the tensors flow

License:        Apache 2.0
URL:            https://www.tensorflow.org/
Source0:        https://github.com/tensorflow/tensorflow/archive/v%{version}.tar.gz

BuildRequires:  gcc-c++
BuildRequires:  bazel
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
TensorFlow is an open source software library for numerical computation using
data flow graphs.

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
TensorFlow is an open source software library for numerical computation using
data flow graphs. This package contains the python3 version of this module.


%prep
%setup -q -c -n %{name}-%{version}

%build
#%%py3_build
./configure

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
