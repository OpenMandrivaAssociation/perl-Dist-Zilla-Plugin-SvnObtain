%define upstream_name    Dist-Zilla-Plugin-SvnObtain
%define upstream_version 0.02

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Obtain files from a subversion repository before building a distribution
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Cwd)
BuildRequires:	perl(Dist::Zilla::Role::BeforeBuild)
BuildRequires:	perl(Dist::Zilla::Role::Plugin)
BuildRequires:	perl(File::Path)
BuildRequires:	perl(Moose)
BuildRequires:	perl(SVN::Client)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
Uses the SVN::Client manpage to obtain files from a subversion repository
for inclusion in a distribution made with the Dist::Zilla manpage.

'[SvnObtain]' sections in your _dist.ini_ file describe a set of Subversion
repositories that will be downloaded into the current directory prior to
building a distribution. Subdirectories will be created that correspond to
the name of the projects listed in that section. Optionally, after the URL
of the subversion repository, you may specify a particular revision to
check out. If you do not specify a revision, 'HEAD' will be used. For
instance, to include a copy MIT's simile timeline widget into your
distribution, your _dist.ini_ would contain something like this:

  [SvnObtain]
    simile = http://simile-widgets.googlecode.com/svn

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

