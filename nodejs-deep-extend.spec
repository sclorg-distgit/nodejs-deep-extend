%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global module_name deep-extend

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        0.4.1
Release:        2%{?dist}
Summary:        Recursive object extending
License:        MIT
URL:            https://github.com/unclechu/node-deep-extend
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(mocha)
BuildRequires:  %{?scl_prefix}npm(should)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr lib package.json *.js %{buildroot}%{nodejs_sitelib}/%{module_name}
%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
mocha
%endif

%files
%{!?_licensedir:%global license %doc}
%doc README.md LICENSE
%{nodejs_sitelib}/%{module_name}

%changelog
* Mon Nov 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.4.1-2
- Copy lib dir in %%install

* Mon Oct 31 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.4.1-1
- Updated with script

* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.2-7
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.2-6
- Rebuilt with updated metapackage

* Wed Jan 13 2016 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-5
- Enable scl macros

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-4
- Use macro to find provides and requires

* Tue Jan 12 2016 Tomas Hrcka <thrcka@redhat.com> - 0.3.2-3
- Enable scl macros, fix license macro for el6

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 04 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.3.2-1
- Initial packaging
